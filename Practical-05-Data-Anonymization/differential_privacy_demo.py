import random
import math

def laplace_noise(scale):
    # Inverse-CDF sampling for Laplace noise.
    u = random.uniform(-0.5, 0.5)
    return -scale * math.copysign(math.log(1 - 2 * abs(u)), u)

def noisy_count(true_count, epsilon=1.0):
    # Educational differential-privacy-style demonstration.
    # Sensitivity is assumed to be 1, so scale = sensitivity / epsilon.
    scale = 1 / epsilon
    return true_count + laplace_noise(scale)

true_count = 100
epsilon = 1.0

print("True count:", true_count)
for i in range(5):
    print(f"Noisy result {i+1}: {noisy_count(true_count, epsilon):.2f}")

print("\nNote: This is a simplified teaching demonstration, not a production DP library.")
