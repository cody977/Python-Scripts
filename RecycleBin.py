import winshell


#FUNCTIONS
def empty_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=False)
        print("Recycle bin emptied successfully.")
    except Exception as e:
        print(f" [empty_recycle_bin] An error occurred: {e}")


def list_recycle_bin_files():
    try:
        recycle_bin_content = list(winshell.recycle_bin())
        if recycle_bin_content:
            print("Files in Recycle Bin:")
            for item in recycle_bin_content:
                print(item.original_filename())
        else:
            print("Recycle Bin is empty.")
    except Exception as e:
        print(f"[list_recycle_bin_files] An error occurred: {e}")




#MAIN
if __name__ == "__main__":
    list_recycle_bin_files()

    input("Press Enter to empty the recycle bin...")
    empty_recycle_bin()
