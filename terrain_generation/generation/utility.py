def normalize_noise(noise) -> None:
    min_value = noise.min()
    max_value = noise.max()
    for i in range(len(noise)):
        for j in range(len(noise)):
            noise[i][j] = (noise[i][j] - min_value) / (max_value - min_value)
