import os
import hashlib
import shutil
import time
import argparse
import logging


def compute_md5(file_path):
    """Compute MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def sync_folders(source, replica, logger):
    """Synchronize replica folder with source folder."""
    # Ensure all files and folders in source are present in replica
    for root, dirs, files in os.walk(source):
        # Compute relative path
        relative_path = os.path.relpath(root, source)
        replica_dir = os.path.join(replica, relative_path)

        # Ensure directory exists in replica
        if not os.path.exists(replica_dir):
            os.makedirs(replica_dir)
            logger.info(f"Created directory: {replica_dir}")
            print(f"Created directory: {replica_dir}")

        # Copy files
        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_dir, file)

            if not os.path.exists(replica_file) or compute_md5(source_file) != compute_md5(replica_file):
                shutil.copy2(source_file, replica_file)
                logger.info(f"Copied/Updated file: {replica_file}")
                print(f"Copied/Updated file: {replica_file}")

    # Ensure all files and folders in replica match source
    for root, dirs, files in os.walk(replica):
        # Compute relative path
        relative_path = os.path.relpath(root, replica)
        source_dir = os.path.join(source, relative_path)

        # Remove directories not in source
        for dir in dirs:
            if not os.path.exists(os.path.join(source_dir, dir)):
                shutil.rmtree(os.path.join(root, dir))
                logger.info(f"Removed directory: {os.path.join(root, dir)}")
                print(f"Removed directory: {os.path.join(root, dir)}")

        # Remove files not in source
        for file in files:
            if not os.path.exists(os.path.join(source_dir, file)):
                os.remove(os.path.join(root, file))
                logger.info(f"Removed file: {os.path.join(root, file)}")
                print(f"Removed file: {os.path.join(root, file)}")


def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source", help="Source folder path")
    parser.add_argument("replica", help="Replica folder path")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("logfile", help="Log file path")

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(filename=args.logfile, level=logging.INFO, format="%(asctime)s - %(message)s")
    logger = logging.getLogger()

    source = args.source
    replica = args.replica
    interval = args.interval

    while True:
        logger.info("Starting synchronization.")
        print("Starting synchronization.")
        sync_folders(source, replica, logger)
        logger.info("Synchronization complete.")
        print("Synchronization complete.")
        time.sleep(interval)


if __name__ == "__main__":
    main()
