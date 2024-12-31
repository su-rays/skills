import cv2
import numpy as np

class OpencvPython:
    def __init__(self, source="people_walking.mp4"):
        self.source = source
        self.cap = None

    def __enter__(self):
        self.cap_source()
        return self

    def __exit__(self, exe_type, exe_value, traceback):
        self.release_source()
        if exe_type:
            print(f"An exception occurred: {exe_value}")

    def __iter__(self):
        return self

    def __next__(self):
        return self.read_frame()

    def cap_source(self):
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open video source: {self.source}")
        print(f"Video source '{self.source}' opened successfully.")

    def read_frame(self):
        if not self.cap or not self.cap.isOpened():
            raise StopIteration
        ret, frame = self.cap.read()
        if not ret:
            print("End of video or unable to capture frame.")
            self.release_source()
            raise StopIteration
        return frame

    def release_source(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
            print(f"Video source '{self.source}' released.")

    def convert_to_grayscale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def apply_gaussian_blur(self, frame, kernel_size=(5, 5)):
        return cv2.GaussianBlur(frame, kernel_size, 0)

    def detect_edges(self, frame, threshold1=50, threshold2=150):
        return cv2.Canny(frame, threshold1, threshold2)

    def draw_contours(self, frame):
        gray = self.convert_to_grayscale(frame)
        edges = self.detect_edges(gray)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return cv2.drawContours(frame.copy(), contours, -1, (0, 255, 0), 2)

    def add_text(self, frame, text, position=(50, 50), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 255, 0), thickness=2):
        return cv2.putText(frame, text, position, font, font_scale, color, thickness)

    def resize_frame(self, frame, width, height):
        return cv2.resize(frame, (width, height))

    def rotate_frame(self, frame, angle):
        height, width = frame.shape[:2]
        center = (width // 2, height // 2)
        matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(frame, matrix, (width, height))

    def flip_frame(self, frame, flip_code):
        return cv2.flip(frame, flip_code)

    def apply_threshold(self, frame, thresh_value=127):
        gray = self.convert_to_grayscale(frame)
        _, thresholded = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)
        return thresholded

    def detect_faces(self, frame, face_cascade_path="haarcascade_frontalface_default.xml"):
        gray = self.convert_to_grayscale(frame)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame

    def write_video(self, frames, output_path, fps=20, frame_size=(640, 480)):

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)
        for frame in frames:
            resized_frame = self.resize_frame(frame, 640, 480)
            out.write(resized_frame)
        out.release()
        print(f"Video saved to {output_path}")

if __name__ == "__main__":
    with OpencvPython() as vs:
        try:
            frames_original = []
            frames_gray = []
            frames_blurred = []
            frames_edges = []

            for frame in vs:
                gray_frame = vs.convert_to_grayscale(frame)
                blurred_frame = vs.apply_gaussian_blur(gray_frame)
                edges_frame = vs.detect_edges(blurred_frame)

                frames_original.append(frame)
                frames_gray.append(cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR))
                frames_blurred.append(cv2.cvtColor(blurred_frame, cv2.COLOR_GRAY2BGR))
                frames_edges.append(cv2.cvtColor(edges_frame, cv2.COLOR_GRAY2BGR))

                frames_edges.append(cv2.cvtColor(edges_frame, cv2.COLOR_GRAY2BGR))

                cv2.imshow("Original", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            vs.write_video(frames_original, "opencv_videos/output_original.avi")
            vs.write_video(frames_gray, "opencv_videos/output_gray.avi")
            vs.write_video(frames_blurred, "opencv_videos/output_blurred.avi")
            vs.write_video(frames_edges, "opencv_videos/output_edges.avi")
        finally:
            cv2.destroyAllWindows()
