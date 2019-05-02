from __future__ import print_function
import os
import sys
import operator


def null_decorator(ob):
    return ob


if sys.version_info >= (3, 2, 0):
    import functools

    my_cache_decorator = functools.lru_cache(maxsize=4096)
else:
    my_cache_decorator = null_decorator

start_dir = os.path.normpath(os.path.abspath(sys.argv[1])) if len(sys.argv) > 1 else 'C:\\Program Files (x86)\\'


@my_cache_decorator
def get_dir_size(start_path='.'):
    total_size = 0
    if 'scandir' in dir(os):
        # using fast 'os.scandir' method (new in version 3.5)
        for entry in os.scandir(start_path):
            if entry.is_dir(follow_symlinks=False):
                total_size += get_dir_size(entry.path)
            elif entry.is_file(follow_symlinks=False):
                total_size += entry.stat().st_size
    else:
        # using slow, but compatible 'os.listdir' method
        for entry in os.listdir(start_path):
            full_path = os.path.abspath(os.path.join(start_path, entry))
            if os.path.isdir(full_path):
                total_size += get_dir_size(full_path)
            elif os.path.isfile(full_path):
                total_size += os.path.getsize(full_path)
    return total_size


def get_dir_size_walk(start_path='C:\\Program Files (x86)\\'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def bytes2human(n, format='%(value).0f%(symbol)s', symbols='customary'):
    symb = {
        'customary': ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'),
        'customary_ext': ('byte', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa',
                          'zetta', 'iotta'),
        'iec': ('Bi', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi'),
        'iec_ext': ('byte', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi',
                    'zebi', 'yobi'),
    }
    n = int(n)
    if n < 0:
        raise ValueError("n < 0")
    symbols = symb[symbols]
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i + 1) * 10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)


# main ()
if __name__ == '__main__':
    dir_tree = {}
    get_size = get_dir_size

    for root, dirs, files in os.walk(start_dir):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if os.path.isdir(dir_path):
                dir_tree[dir_path] = get_size(dir_path)

    for d, size in sorted(dir_tree.items(), key=operator.itemgetter(1), reverse=True):
        print('%s\t%s' % (bytes2human(size, format='%(value).2f%(symbol)s'), d))

    print('-' * 80)
    if sys.version_info >= (3, 2, 0):
        print(get_dir_size.cache_info())
