# music_teacher.py

class MusicTeacher:
    def __init__(self):
        self.scales = {
            "C Major": ["C", "D", "E", "F", "G", "A", "B"],
            "G Major": ["G", "A", "B", "C", "D", "E", "F#"],
            "D Major": ["D", "E", "F#", "G", "A", "B", "C#"],
            "A Minor": ["A", "B", "C", "D", "E", "F", "G"],
        }

    def list_scales(self):
        print("Available scales:")
        for scale in self.scales:
            print(f"- {scale}")

    def play_scale(self, scale_name):
        if scale_name in self.scales:
            notes = self.scales[scale_name]
            print(f"The {scale_name} scale contains the following notes:")
            print(" -> ".join(notes))
        else:
            print(f"Scale '{scale_name}' not found. Please choose from the list below.")
            self.list_scales()

if __name__ == "__main__":
    teacher = MusicTeacher()
    print("Welcome to the Music Teacher App!")
    teacher.list_scales()

    while True:
        choice = input("\nEnter the name of a scale to learn it, or 'exit' to quit: ").strip()
        if choice.lower() == "exit":
            print("Goodbye! Keep practicing your scales!")
            break
        teacher.play_scale(choice)


## Contributing
Contributions are welcome! Feel free to submit pull requests with new features, such as:
- Adding more scales.
- Supporting minor scales.
- Including playback of scales with sound.

## License
MIT
