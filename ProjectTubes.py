# Definisi Proyek
class Project:
    def __init__(self, name, deadline, priority, duration):
        self.name = name
        self.deadline = deadline
        self.priority = priority
        self.duration = duration

    def __repr__(self):
        return f"{self.name}(Deadline: {self.deadline}, Priority: {self.priority}, Duration: {self.duration})"

# Merge Sort untuk mengurutkan proyek berdasarkan tenggat waktu
def merge_sort(projects):
    if len(projects) <= 1:
        return projects

    mid = len(projects) // 2
    left = merge_sort(projects[:mid])
    right = merge_sort(projects[mid:])
    
    sorted_projects = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].deadline < right[j].deadline:
            sorted_projects.append(left[i])
            i += 1
        else:
            sorted_projects.append(right[j])
            j += 1

    sorted_projects.extend(left[i:])
    sorted_projects.extend(right[j:])
    return sorted_projects

# Greedy Algorithm untuk memilih proyek
def schedule_projects(projects):
    projects = merge_sort(projects)  # Mengurutkan proyek terlebih dahulu
    scheduled = []
    current_time = 0

    for project in projects:
        if current_time + project.duration <= project.deadline:
            scheduled.append(project)
            current_time += project.duration
    
    return scheduled

# Contoh Data Proyek
projects = [
    Project("Proyek A", 4, 2, 2),
    Project("Proyek B", 1, 1, 1),
    Project("Proyek C", 3, 3, 2),
    Project("Proyek D", 2, 2, 1),
    Project("Proyek E", 5, 1, 3)
]

# Menjadwalkan proyek menggunakan Greedy Algorithm
scheduled = schedule_projects(projects)

# Menampilkan Proyek yang Dijadwalkan
print("Proyek yang Dijadwalkan:")
for p in scheduled:
    print(p)