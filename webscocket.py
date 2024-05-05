import websocket
import json
import cv2
import base64

device_code = "1001"

def on_message(ws, message):
    print("Received message:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Connection closed:", close_status_code, close_msg)


def capture_image_and_send(ws):
    # Accessing the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, convert it to base64 and send
    if ret:
        _, img_encoded = cv2.imencode('.jpg', frame)
        image_base64 = base64.b64encode(img_encoded).decode('utf-8')
        # Send the image to the WebSocket server
        ws.send(json.dumps({
            "command": "send_image",
            "room_code": device_code,  # Replace with your room code
            "image_data": image_base64
        }))
        print("Image sent successfully")

    # Release the capture
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

def main():
    uri = "ws://localhost:8000/images/"
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(uri,on_message=on_message,on_error=on_error,on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

def on_open(ws):
    # Send a command to join a room
    ws.send(json.dumps({
        "command": "join_room",
        "room_code": device_code  # Replace with your room code
    }))
    
    print("Joined room successfully")
    capture_image_and_send(ws)

if __name__ == "__main__":
    main()
