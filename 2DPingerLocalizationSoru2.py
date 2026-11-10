import numpy as np
# Her açı grubu aynı sıradaki robot konumuna ait.
positions = [[0, 0], [12, 0], [12, 10], [0, 10]]
angle_samples = [
[45, 47, 49, 51, 53, -70, 145],
[114, 116, 118, 120, 122, 20, -50],
[-135, -133, -131, -129, -127, -20, 50],
[-41, -39, -37, -35, -33, 70, -150],
]
def filter_angles(angle_groups):

	ortalamalar = []

	for grup in angle_groups:
		medyan = np.median(grup)
		ortalamalar.append(medyan)


	return ortalamalar

# Hazır yardımcı fonksiyon: değiştirmeniz gerekmiyor.
def estimate_position(positions, angles):
	A, b = [], [] # Her konum ve açıdan bir doğru denklemi kuracağız.
	for i in range(len(positions)):
		x, y = positions[i]
		theta = np.deg2rad(angles[i]) # Sinüs ve kosinüs radyan kullanır.
		# Ölçülen yöne dik bir vektör: doğrunun normalini buluyoruz.
		nx = -np.sin(theta)
		ny = np.cos(theta)
		# Pinger (px, py) için: nx*px + ny*py = nx*x + ny*y.
		A.append([nx, ny])
		b.append(nx * x + ny * y)
	# Doğrular tam kesişmese de hepsine en yakın noktayı bulur.
	position, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
	return position # Tahmini pinger konumu: [x, y].
if __name__ == "__main__":
	angles = filter_angles(angle_samples)
	position = estimate_position(positions, angles)
	print("Ortalama açılar (derece):", angles)
	print("Tahmini pinger konumu (m):", position)