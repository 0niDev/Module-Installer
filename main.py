import threading
from os import system
from time import perf_counter


def main():
    try:
        NumberOfThreads = int(input("Enter the number of threads: "))
    except ValueError:
        pass
    t1 = perf_counter()
    with open("modules.txt", "r") as f:
        modules = f.read().splitlines()
    ModulesPerThreads = dividing(modules, NumberOfThreads)
    threads = []
    for i in range(NumberOfThreads):
        threads.append(
            threading.Thread(target=threadTask, args=(ModulesPerThreads[i],))
        )
    for i in threads:
        i.start()
    for i in threads:
        i.join()
    t2 = perf_counter()
    print(f"Time taken: {t2 - t1} seconds")
    input("Press Enter to exit...")


def threadTask(Modules):
    system(f"python.exe -m pip install --upgrade p")
    for i in Modules:
        system(f"pip install --user {i}")


def dividing(modules: list, NumberOfThreads=10):
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
