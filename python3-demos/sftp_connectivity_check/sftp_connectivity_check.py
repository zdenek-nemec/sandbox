import collections
import csv
import paramiko


TARGETS_FILE = "targets.csv"
PRIVATE_KEY = "path/to/private_key"


def main():
    print("Hello, SFTP Connectivity Check!")

    Target = collections.namedtuple("Target", ["user", "host", "port"])

    target_list = []
    with open(TARGETS_FILE, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            target_list.append(Target(row[0], row[1], int(row[2])))

    for target in target_list:
        try:
            transport = paramiko.Transport((target.host, target.port))
        except:
            connectivity_test = False
            login_test = False
        else:
            connectivity_test = True

        if connectivity_test:
            try:
                rsa_key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY)
                transport.connect(username=target.user, pkey=rsa_key)
                sftp = paramiko.SFTPClient.from_transport(transport)
            except:
                login_test = False
            else:
                login_test = True
                sftp.close()
            finally:
                transport.close()

        print("%s@%s, %s, %s" % (target.user, target.host, connectivity_test, login_test))


if __name__ == "__main__":
    main()
