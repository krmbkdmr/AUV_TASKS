# Sentetik jiroskop verileri: her satır [wx, wy, wz], birim rad/s.
# Kalibrasyon sırasında sensör hareketsizdir.
calibration_data = [
[0.019, -0.009, 0.031],
[0.021, -0.011, 0.029],
[0.018, -0.012, 0.032],
[0.022, -0.008, 0.028],
]
test_data = [
[0.120, -0.010, 0.030],
[0.020, 0.090, 0.030],
[0.020, -0.010, 0.030],
]
def calculate_bias(samples):

	if len(samples) == 0:
		raise ValueError("Liste Boş olmamalı.")

	bx = sum(sample[0] for sample in samples) / len(samples)
	by = sum(sample[1] for sample in samples) / len(samples)
	bz = sum(sample[2] for sample in samples) / len(samples)
	return[bx,by,bz]

def correct_measurements(samples, bias):
	dogrulanan = []
	for sample in samples:
		dx= sample[0] - bias[0]
		dy= sample[1] - bias[1]
		dz= sample[2] - bias[2]

		dogrulanan.append([dx,dy,dz])
	return dogrulanan

if __name__ == "__main__":
	bias = calculate_bias(calibration_data)
	corrected_measurements = correct_measurements(test_data, bias)
	print("Bias (rad/s):", bias)
	print("Düzeltilmiş ölçümler (rad/s):")
	for olcumler in corrected_measurements:
		print(olcumler)