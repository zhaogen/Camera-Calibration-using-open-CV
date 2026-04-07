import numpy as np
import cv2

# 1. 체스보드 설정 (교차점 개수)
CHESS_W = 8
CHESS_H = 5

objp = np.zeros((CHESS_W * CHESS_H, 3), np.float32)
objp[:, :2] = np.mgrid[0:CHESS_W, 0:CHESS_H].T.reshape(-1, 2)

objpoints = [] 
imgpoints = [] 


cap = cv2.VideoCapture('board.mp4')
last_gray_shape = None 

# --- 화면 크기 조절 설정 ---
cv2.namedWindow('Calibration Process', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('Calibration Process', 800, 600) # 보기 편한 크기로 조절
# ------------------------

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    last_gray_shape = gray.shape[::-1] 
    
    # 코너 찾기
    ret_corners, corners = cv2.findChessboardCorners(gray, (CHESS_W, CHESS_H), None)

    if ret_corners:
        objpoints.append(objp)
        imgpoints.append(corners)
        # 화면에 코너 표시
        cv2.drawChessboardCorners(frame, (CHESS_W, CHESS_H), corners, ret_corners)
    
    cv2.imshow('Calibration Process', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

# 3. 캘리브레이션 수행
if len(objpoints) > 10: # 충분한 데이터(최소 10프레임 이상)가 쌓였을 때 실행
    print("계산 중... 잠시만 기다려주세요.")
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, last_gray_shape, None, None)

    print("\n--- Calibration Results ---")
    print(f"RMS Error: {ret}") # 이 값이 낮을수록 정확합니다
    print(f"Intrinsic Matrix (K):\n{mtx}")
    print(f"Distortion Coefficients:\n{dist}")

    np.savez("calib_result.npz", mtx=mtx, dist=dist)
    print("\n결과가 'calib_result.npz'에 저장되었습니다.")
else:
    print(f"검출된 프레임 수({len(objpoints)})가 너무 적습니다. 영상을 끝까지 재생하거나 더 천천히 찍어주세요.")