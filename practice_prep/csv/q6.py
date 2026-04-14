import json
def filter_completed_tasks(input_file ,output_file):
    try :
        with open(input_file, "r", encoding='utf-8') as file:
            all_taskd = json.load(file)

        completed = [task for task in all_tasks if task.get("status") == "done"]
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(completed, file, indent=4)
        print(f"success! Found {len(completed)} completed task")
        print(f"saved to{output_file}")
    except: pass
