"""Problem 1
While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?
"""

"""Problem 2
You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
How many IPs in your puzzle input support SSL?
"""
import re


def is_abba(s):
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def is_aba(s):
    return s[0] == s[2] and s[0] != s[1]


def supports_tls(ip):
    hypernet = re.findall(r"\[([a-z]+)\]", ip)
    supernet = re.split(r"\[[a-z]+\]", ip)
    for h in hypernet:
        if any(is_abba(h[i : i + 4]) for i in range(len(h) - 3)):
            return False
    for s in supernet:
        if any(is_abba(s[i : i + 4]) for i in range(len(s) - 3)):
            return True

    return False


def support_ssl(ip):
    hypernet = re.findall(r"\[([a-z]+)\]", ip)
    supernet = re.split(r"\[[a-z]+\]", ip)
    abas = []
    for s in supernet:
        for i in range(len(s) - 2):
            if is_aba(s[i : i + 3]):
                abas.append(s[i : i + 3])
    for h in hypernet:
        for i in range(len(h) - 2):
            if h[i] == h[i + 2] and h[i] != h[i + 1]:
                if h[i + 1] + h[i] + h[i + 1] in abas:
                    return True
    return False


with open("inputs/7.txt") as f:
    ip_addrs = f.read().splitlines()

solution = sum(supports_tls(ip) for ip in ip_addrs)
print("Solution 1:", solution)

solution = sum(support_ssl(ip) for ip in ip_addrs)
print("Solution 2:", solution)
