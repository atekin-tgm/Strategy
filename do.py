from engines import *
import argparse

# NOT FINISHED! NO IDEA!!
if __name__ == "__main__":


    help_h = "-h, --help Shows this help"
    help_d = "-d DESTDIR, --dest-dir=DESTDIR Output destination directory (default=Current Working Directory)"
    help_s = "-s SOURCEDIR, --source-dir=SOURCEDIR Input root directory (default=Current Working Directory)"
    help_a = "-a ARCHIVE, --archive-engine=ARCHIVE use the given archive engine (default=ZIP_STORED)"
    help_n = "-n NAME, --archive-name=NAME name of the archive (default=archive)"

    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dest-dir", action="store", help="Output destination directory (default=Current Working Directory)")
    parser.add_argument("-s", "--source-dir", action="store", help="Input root directory (default=Current Working Directory)")
    parser.add_argument("-a", "--archive-engine", action="store", help="use the given archive engine (default=ZIP_STORED)")
    parser.add_argument("-n", "--archive-name", action="store", help="name of the archive (default=archive)")

    args = parser.parse_args()