from animal_dataset import Animal

dataset = Animal(root_path="Dataloader Dataset", batch_size=3)

print("Dataset size:", len(dataset))

batch = dataset.get_item()
print("Batch paths:", batch)

dataset._show_image(batch)
