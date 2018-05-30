#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__all__ = ['imei_fix', 'meid_fix', 'id_fix']

decimal_decoder = lambda s: int(s, 10)
decimal_encoder = lambda i: str(i)

hex_alphabet = '0123456789abcdef'
hex_encoder = lambda i: hex_alphabet[i]
hex_decoder = lambda s: hex_alphabet.index(s)


def luhn_sum_mod_base(string, base=10, decoder=decimal_decoder):
    # Adapted from http://en.wikipedia.org/wiki/Luhn_algorithm
    digits = list(map(decoder, string))
    return (sum(digits[::-2]) + sum(list(map(lambda d: sum(divmod(2 * d, base)), digits[-2::-2])))) % base


def generate(string, base=10, encoder=decimal_encoder, decoder=decimal_decoder):
    d = luhn_sum_mod_base(string + encoder(0), base=base, decoder=decoder)
    if d != 0:
        d = base - d
    return encoder(d)


def verify(string, base=10, decoder=decimal_decoder):
    return luhn_sum_mod_base(string, base=base, decoder=decoder) == 0


def imei_fix(string):
    try:
        if len(string) > 13:
            return string[:14] + generate(string[:14])
        else:
            return ''
    except:
        return ''


def meid_fix(string):
    lower = string.lower()
    try:
        if len(lower) > 13:
            return lower[:14] + generate(lower[:14], base=16, encoder=hex_encoder, decoder=hex_decoder)
        else:
            return ''
    except:
        return ''


def id_fix(string):
    lower = string.lower()
    if 'a' in list(lower) or 'b' in list(lower) or 'c' in list(lower) or 'd' in list(lower) or 'e' in list(lower):
        return meid_fix(lower)
    else:
        return imei_fix(lower)


if __name__ == '__main__':
    print(id_fix('35212305070632'))
    print(id_fix('A1000041B6D402E'))
    print(id_fix('000000013341045'))
