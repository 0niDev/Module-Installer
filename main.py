import threading
from os import system, getcwd, path
from time import perf_counter


def main():
    try:
        NumberOfThreads = int(input("Enter the number of threads: "))
    except ValueError:
        NumberOfThreads = 8
    t1 = perf_counter()
    try:
        with open(path.join(getcwd(), "modules.txt"), "r") as f:
            modules = f.read().splitlines()
    except FileNotFoundError:
        print("Modules.txt was not found")
    if len(modules) > 0:
        ModulesPerThreads = dividing(modules, NumberOfThreads)
        system(f"python.exe -m pip install --upgrade p")
        threads = []
        for i in range(NumberOfThreads):
            threads.append(
                threading.Thread(target=threadTask, args=(ModulesPerThreads[i], i))
            )
        for i in threads:
            i.start()
        for i in threads:
            i.join()
        t2 = perf_counter()
        print(f"Time taken: {t2 - t1} seconds")
        input("Press Enter to exit...")
    else:
        print("Modules.txt is empty")


def threadTask(Modules: list, NumberOfThread):
    for i in Modules:
        print(
            f"\n----------------------------Installing {i}, ({Modules.index(i) * NumberOfThread})-------------------------------------\n"
        )
        system(f"pip install --user {i}")


def dividing(modules: list, NumberOfThreads):
    ModulesPerThread = int(len(modules) / NumberOfThreads)
    ModulesPerThreads = []
    for i in range(NumberOfThreads):
        ModulesPerThreads.insert(
            i, modules[ModulesPerThread * i : ModulesPerThread * (i + 1)]
        )
    ModulesPerThreads[-1].extend(modules[-(len(modules) % NumberOfThreads) : :])
    return ModulesPerThreads


if __name__ == "__main__":
    main()
