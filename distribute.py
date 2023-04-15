import zipfile
import glob
import os

DATAPACK_PATTERNS = [
    "**/*.mcfunction",
    "**/*.mcmeta",
    "**/*.png",
    "**/*.json",
    "**/*.txt", # comments
    "**/*.nbt", # structure files
]
WORLD_PATTERNS = [
    "**/*.mca", # region files
]

def get_files(
    base_folder: str,
    path_list: list[str],
    patterns: list[str],
) -> list[str]:
    files = []
    folders = []
    
    for path in path_list:
        if os.path.isfile(os.path.join(base_folder, path)):
            files.append(path)
        elif os.path.isdir(os.path.join(base_folder, path)):
            folders.append(path)

    for pattern in patterns:
        for folder in folders:
            files.extend(
                [
                    os.path.join(folder, file)
                    for file in glob.glob(
                        pattern,
                        root_dir=os.path.join(base_folder, folder),
                        recursive=True,
                    )
                ]
            )

    return files

def get_world_files() -> list[str]:
    return get_files(
        ".",
        [
            "datapacks",
            "region",
            "icon.png",
            "level.dat",
            "LICENSE.md",
            "README.md",
        ],
        DATAPACK_PATTERNS + WORLD_PATTERNS,
    )

def get_datapack_files() -> list[str]:
    return get_files(
        "datapacks/Bookshelf",
        [
            "data",
            "icon.png",
            "pack.mcmeta",
        ],
        DATAPACK_PATTERNS,
    )

def get_core_datapack_files() -> list[str]:
    return get_files(
        "datapacks/Bookshelf",
        [
            "data/bs.core",
            "data/minecraft",
            "icon.png",
            "pack.mcmeta",
        ],
        DATAPACK_PATTERNS,
    )

def get_module_datapack_files(module_name: str) -> list[str]:
    return get_core_datapack_files() + \
        get_files(
            "datapacks/Bookshelf",
            [
                f"data/bs.{module_name}",
            ],
            DATAPACK_PATTERNS,
        )

def create_archive(filename: str, base_folder: str, files: list[str]):
    archive = zipfile.ZipFile(
        filename,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
    )

    for file in files:
        archive.write(
            filename=os.path.join(base_folder, file),
            arcname=file,
        )

def list_modules() -> list[str]:
    modules = os.listdir("datapacks/Bookshelf/data")
    modules.remove("bs")
    modules.remove("bs.core")
    modules.remove("minecraft")

    return [module[3:] for module in modules]

if __name__ == "__main__":
    if not os.path.exists("./build"):
        os.mkdir("build")
    print("🏞 Creating world archive")
    create_archive(
        "build/Demo-world.zip",
        ".",
        get_world_files(),
    )

    print("🗄 Creating datapack archive")
    create_archive(
        "build/Bookshelf-release.zip",
        "datapacks/Bookshelf",
        get_datapack_files(),
    )

    print("🔩 Creating core module archive")
    create_archive(
        "build/Bookshelf-core.zip",
        "datapacks/Bookshelf",
        get_core_datapack_files(),
    )

    for module in list_modules():
        print(f"🧩 Creating archive for module {module}")
        create_archive(
            f"build/Bookshelf-{module}.zip",
            "datapacks/Bookshelf",
            get_module_datapack_files(module),
        )
