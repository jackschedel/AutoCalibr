import os
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import dataloader


# Define a custom dataset to store the encoded files
class FileDataset:
    def __init__(self, folder_path):
        self.encoded_files = []
        self.max_length = 0
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as f:
                content = f.read()
                length = len(content)
                self.max_length = max(self.max_length, length)
                self.encoded_files.append(content)

    def __len__(self):
        return len(self.encoded_files)

    def __getitem__(self, idx):
        file = self.encoded_files[idx]
        length = len(file)
        encoded = np.zeros(self.max_length, dtype=np.int64)
        encoded[:length] = np.frombuffer(file, dtype=np.uint8)
        return encoded


# Define the encoder
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.embedding = nn.Embedding(input_dim, hidden_dim)

    def forward(self, x):
        return self.embedding(x)


# Define the decoder
class Decoder(nn.Module):
    def __init__(self, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding(hidden_dim, output_dim)

    def forward(self, x):
        return self.embedding(x)


# Define the autoencoder
class Autoencoder(nn.Module):
    def __init__(self, encoder, decoder):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded


# Create a FileDataset object and set the hyperparameters
dataset = FileDataset('../trainingSet/fbx')
input_dim = 256
hidden_dim = 128

# Initialize the encoder, decoder, and autoencoder
encoder = Encoder(input_dim, hidden_dim)
decoder = Decoder(hidden_dim, input_dim)
autoencoder = Autoencoder(encoder, decoder)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(autoencoder.parameters(), lr=0.001)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


num_epochs = 1


while num_epochs != 1:

    while True:
        try:
            # num_epochs = int(input("Enter the number of epochs to run until the next break: "))
            break
        except ValueError:
            print("Invalid input, please enter an integer value for the number of epochs.")


if num_epochs == 1:
    # Train the autoencoder
    for epoch in range(num_epochs):
        for i, data in enumerate(dataset):
            # Zero the gradients
            optimizer.zero_grad()

            # Forward pass
            outputs = autoencoder(torch.from_numpy(data).to(device))
            loss = criterion(outputs)

            # Backward pass and optimization
            loss.backward()
            optimizer.step()

        print("Epoch {}/{} - Loss: {:.4f}".format(epoch + 1, num_epochs, loss.item()))




# Save the trained model
torch.save(autoencoder.state_dict(), "trained_autoencoder.pth")