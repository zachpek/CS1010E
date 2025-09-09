def towers(n, src, tmp, dst):
    if n > 0:
        towers(n - 1, src, dst, tmp)
        print(f'Move disk {n} from {src} to {dst}')
        towers(n - 1, tmp, src, dst)