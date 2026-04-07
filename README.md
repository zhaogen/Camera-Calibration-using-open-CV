Camera Calibration & Lens Distortion Correction
1. 개요 (Introduction)
목적: 체스보드 패턴을 이용하여 스마트폰 카메라의 내부 파라미터와 왜곡 계수를 산출하고, 이를 바탕으로 광각 렌즈의 왜곡을 보정함.

사용 기기: 아이폰 13 Pro (초광각 모드 활용)

환경: Python 3.12 (Anaconda), OpenCV 4.x

2. 카메라 캘리브레이션 (Camera Calibration)
2.1 수행 과정A4 용지에 출력된 $9 \times 6$ 체스보드(내부 교차점 $8 \times 5$)를 다양한 각도와 거리에서 촬영함.cv2.findChessboardCorners를 사용하여 각 프레임의 코너 좌표를 검출함.검출된 2D 이미지 좌표와 3D 공간 좌표를 매칭하여 카메라 행렬을 산출함.
   
2.2 산출 결과수행 결과 얻은 카메라의 고유 파라미터는 다음과 같습니다.
  RMS Error (평균 제곱근 오차): 1.039
Intrinsic Matrix (K) - 내부 파라미터:$f_x$ (가로 초점 거리): 866.03$f_y$ (세로 초점 거리): 866.65$c_x$ (주점 X좌표): 534.08$c_y$ (주점 Y좌표): 958.30Distortion Coefficients (왜곡 계수):[-0.0116747, -0.00834635, -0.00071855, -0.00183375, 0.00951483]

3. 렌즈 왜곡 보정 (Lens Distortion Correction)
3.1 보정 방법
위 단계에서 구한 mtx(Intrinsic Matrix)와 dist(Distortion Coefficients)를 cv2.undistort 함수에 적용함.

원본 영상과 보정된 영상을 비교하여 직선의 선형성이 회복되었는지 확인함.

원본(original)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/17e687ee-e033-4e50-bc4c-b11b3abc6e83" />



3.2 결과 비교 (Demo)
주요 확인 포인트: 아이폰 광각 특유의 화면 외곽 부분 휘어짐 현상이 보정 후 직선으로 곧게 펴진 것을 확인할 수 있음.

<img width="1002" height="790" alt="image" src="https://github.com/user-attachments/assets/e0d7b210-4bca-4c59-92f5-5334815eae7c" />
