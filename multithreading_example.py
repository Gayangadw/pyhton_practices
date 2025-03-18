import time
import queue
from threading import Thread
import requests
import os

number_of_threads = 5
q = queue.Queue()


def download_image(download_location):
    while True:
        image_url = q.get()
        try:
            res = requests.get(image_url, stream=True, verify=False)
            filename = f"{download_location}/{image_url.split('/')[-1]}.jpg"
            with open(filename, 'wb') as f:
                for block in res.iter_content(1024):
                    f.write(block)
            print(f"Image downloaded successfully: {filename}")
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")
        finally:
            q.task_done()


def download_images_with_multithreading(images):
    print("Starting function with multithreading.")

    # Create directory if it doesn't exist
    if not os.path.exists("with_multithreading_photos"):
        os.makedirs("with_multithreading_photos")

    for image_url in images:
        q.put(image_url)

    for t in range(number_of_threads):
        worker = Thread(target=download_image, args=("with_multithreading_photos",))
        worker.daemon = True
        print(f"Starting {worker.name}")
        worker.start()

    q.join()


def download_images_without_multithreading(images):
    print("Starting function without multithreading or multiprocessing.")

    # Create directory if it doesn't exist
    if not os.path.exists("without_multithreading_photos"):
        os.makedirs("without_multithreading_photos")

    for image_url in images:
        try:
            res = requests.get(image_url, stream=True, verify=False)
            filename = f"without_multithreading_photos/{image_url.split('/')[-1]}.jpg"
            with open(filename, 'wb') as f:
                for block in res.iter_content(1024):
                    f.write(block)
            print(f"Image downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")


def main():
    images = [
        'https://images.unsplash.com/photo-1428366890462-dd4baecf492b',
        'https://images.unsplash.com/photo-1541447271487-09612b3f49f7',
        'https://images.unsplash.com/photo-1560840067-ddcaeb7831d2',
        'https://images.unsplash.com/photo-1522069365959-25716fb5001a',
        'https://images.unsplash.com/photo-1533752125192-ae59c3f8c403',
    ]

    print("Downloading images from the Internet.\n")

    start_time = time.time()
    download_images_with_multithreading(images)
    print("--- Function with multithreading took %s seconds ---\n" % (
            time.time() - start_time))

    start_time = time.time()
    download_images_without_multithreading(images)
    print("--- Function without multithreading took %s seconds ---\n" % (
            time.time() - start_time))


if __name__ == "__main__":
    main()