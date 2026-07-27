from utils.file_manager import FileManager

sample = {
    "project" : "caresight",
    "status" : "working"
}

path = FileManager.save_json(
    data = sample,
    folder = "Test",
    filename= "sample.json",
)

print("saved to..")
print(path)