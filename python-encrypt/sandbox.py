#!/usr/bin/env python3


DEFAULT_MESSAGE = 'HELLO WORLD'
DEFAULT_KEY = ' AZ0'
DEFAULT_ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


class Encryption(object):
    def __init__(self, alphabet):
        self._alphabet = list(alphabet)

    def _decrypt(self, message_value, key_value):
        return (
            (len(self._alphabet) + message_value - key_value) %
            len(self._alphabet))

    def _encrypt(self, message_value, key_value):
        return (message_value + key_value) % len(self._alphabet)

    def _transform(self, message_char, key_char, operation):
        message_value = self._alphabet.index(message_char)
        key_value = self._alphabet.index(key_char)
        transformed_value = operation(message_value, key_value)
        return self._alphabet[transformed_value]

    def _transform_message(self, message, key, operation):
        transformed = ''
        for index in range(0, len(message)):
            message_char = message[index]
            key_char = key[index % len(key)]
            transformed += self._transform(message_char, key_char, operation)
        return transformed

    def decrypt_message(self, message, key):
        return self._transform_message(message, key, self._encrypt)

    def encrypt_message(self, message, key):
        return self._transform_message(message, key, self._decrypt)


def main():
    message_plain = DEFAULT_MESSAGE
    key = DEFAULT_KEY
    alphabet = DEFAULT_ALPHABET

    encryption = Encryption(alphabet)
    print(message_plain)
    message_encrypted = encryption.encrypt_message(message_plain, key)
    print(message_encrypted)
    message_decrypted = encryption.decrypt_message(message_encrypted, key)
    print(message_decrypted)


if __name__ == '__main__':
    main()
