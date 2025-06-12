# Resource Optimization with Python

## ✅ **Exercise 1: Reading and Writing Images with OpenCV**

---

### 🛠️ **Task 1 - Install and Import OpenCV**

#### Step 1: Launch Jupyter Notebook

1. Open **Anaconda Navigator** (in terminal type: `anaconda-navigator`)
2. Launch **Jupyter Notebook** from Anaconda Navigator
3. In Jupyter, click **New > Terminal**

#### Step 2: Install OpenCV

In the terminal, type:

```bash
pip install opencv-python
```

#### Step 3: Create a New Notebook

* In Jupyter, click **New > Python 3**
* Save the notebook: **File > Save As > Using OpenCV.ipynb**

#### Step 4: Import OpenCV

In the first code cell, type:

```python
import cv2 as cv
```

Click **Run** (Shift + Enter).

---

### 🖼️ **Task 2 - Load an Image from File System**

#### Step 1: Download Sample Image

In the **Jupyter Terminal**, type:

```bash
curl https://file-examples-com.github.io/uploads/2017/10/file_example_JPG_500kB.jpg > image-test.jpg
```

#### Step 2: Load the Image Using OpenCV

In the notebook, in a new cell, type:

```python
image = cv.imread('image-test.jpg')  # Default is IMREAD_COLOR
```

Click **Run**.

Optional (to verify image loaded successfully):

```python
if image is not None:
    print("Image loaded successfully")
else:
    print("Error loading image")
```

---

### 💾 **Task 3 - Write Image to File System**

To save a copy of the image:

```python
cv.imwrite('copy-image-test.png', image)
```

Check your Jupyter working directory. You should see **`copy-image-test.png`** there.

---

### ✅ Summary

| Step           | Command                                    | Result                       |
| -------------- | ------------------------------------------ | ---------------------------- |
| Install OpenCV | `pip install opencv-python`                | Installs OpenCV              |
| Import         | `import cv2 as cv`                         | Imports the module           |
| Read Image     | `cv.imread('image-test.jpg')`              | Loads image into NumPy array |
| Write Image    | `cv.imwrite('copy-image-test.png', image)` | Saves image to disk          |

Let me know if you’d like to visualize the image in the notebook or handle grayscale images next!

Here's a **complete guide** for **Exercise 2: Performing Bitwise Operations and Rotation on Images using OpenCV**, broken down clearly so you can follow each step in your Jupyter Notebook:

---

## ✅ **Exercise 2: Bitwise Operations and Image Rotation using OpenCV**

---

### 🛠️ **Task 1 - Import OpenCV and Load Image in Grayscale**

#### Step 1: Install OpenCV (if not already)

In **Jupyter Terminal**:

```bash
pip install opencv-python
```

#### Step 2: Create a new notebook

* **Save As**: `Perform Bitwise and rotate images using OpenCV.ipynb`

#### Step 3: Import OpenCV

In a new cell:

```python
import cv2 as cv
```

#### Step 4: Download and Load the Image

In the **Jupyter Terminal**:

```bash
curl https://file-examples-com.github.io/uploads/2017/10/file_example_JPG_500kB.jpg > image1.jpg
```

In the notebook:

```python
image = cv.imread('image1.jpg', cv.IMREAD_GRAYSCALE)
cv.imwrite('copy-image1.png', image)  # Save grayscale version
```

---

### 🔄 **Task 2 - Rotate Image 90 Degrees Clockwise**

```python
image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
cv.imwrite('test_rotated.jpg', image)
```

---

### 📐 **Task 3 - Use NumPy for Dimensions & Translate Image**

#### Step 1: Import NumPy and Get Dimensions

```python
import numpy as np

rows, cols = image.shape
print(rows, cols)
```

#### Step 2: Create Translation Matrix and Apply Transformation

```python
M = np.float32([[1, 0, 100], [0, 1, 50]])
translated_image = cv.warpAffine(image, M, (cols, rows))
cv.imwrite('translated_image.jpg', translated_image)
```

---

### ⚙️ **Task 4 - Perform Bitwise Operations**

#### Step 1: Create Rectangle Image

```python
image1_bitwise = np.zeros((300, 300), dtype="uint8")
cv.rectangle(image1_bitwise, (100, 100), (250, 250), 255, -1)
cv.imwrite('image1_bitwise.jpg', image1_bitwise)
```

#### Step 2: Create Circle Image

```python
image2_bitwise = np.zeros((300, 300), dtype="uint8")
cv.circle(image2_bitwise, (150, 150), 90, 255, -1)
cv.imwrite('image2_bitwise.jpg', image2_bitwise)
```

#### Step 3: Apply Bitwise AND Operation

```python
bitwise_image = cv.bitwise_and(image1_bitwise, image2_bitwise)
cv.imwrite('bitwise_and_image.jpg', bitwise_image)
```

---

### ✅ **Summary of Output Files**

| Operation         | Output File             |
| ----------------- | ----------------------- |
| Grayscale Image   | `copy-image1.png`       |
| Rotated Image     | `test_rotated.jpg`      |
| Translated Image  | `translated_image.jpg`  |
| Rectangle Image   | `image1_bitwise.jpg`    |
| Circle Image      | `image2_bitwise.jpg`    |
| Bitwise AND Image | `bitwise_and_image.jpg` |

Let me know if you'd like to perform **bitwise OR, XOR, or NOT** operations too, or if you'd like to display images inline in the notebook using `matplotlib`.

Here's a **step-by-step guide** for **Exercise 3: Adding and Blurring Noisy Images and Edges Using OpenCV**, based on your instructions.

---

## ✅ **Exercise 3: Adding and Blurring Noisy Images Using OpenCV**

---

### 🛠️ **Task 1 - Import OpenCV and Load the Image**

#### Step 1: Install OpenCV

In **Jupyter Terminal**:

```bash
pip install opencv-python
```

#### Step 2: Create a New Notebook

* Save it as: **`Adding and blurring noisy images.ipynb`**

#### Step 3: Import OpenCV and Load the Image

In a notebook code cell:

```python
import cv2 as cv
```

#### Step 4: Download and Read the Image

In the **Jupyter Terminal**:

```bash
curl https://www.atwpl.com/learn_python/public/hermoine_granger.jpg > hermoine_granger.jpg
```

In the notebook:

```python
image = cv.imread('hermoine_granger.jpg')
cv.imwrite('copy-hermoine_granger.png', image)
```

---

### 🎯 **Task 2 - Add Gaussian Noise**

#### Step 1: Import NumPy and Add Noise

```python
import numpy as np

row, col, ch = image.shape
mean = 2
var = 5
sigma = var ** 2.5

gauss = np.random.normal(mean, sigma, (row, col, ch))
gauss = gauss.reshape(row, col, ch)

# Ensure the result stays within 0-255 and convert to uint8
noisy_image = np.clip(image + gauss, 0, 255).astype(np.uint8)
cv.imwrite('gauss-noisyimage.jpg', noisy_image)
```

---

### 🧹 **Task 3 - Apply Gaussian and Median Blur**

#### Step 1: Gaussian Blur

```python
image1 = cv.imread('gauss-noisyimage.jpg')
guassian_blur_image = cv.GaussianBlur(image1, (5, 5), 20)
cv.imwrite('guassian_blur_image.jpg', guassian_blur_image)
```

#### Step 2: Median Blur

```python
median_blur_image = cv.medianBlur(image1, 7)
cv.imwrite('median_blur_image.jpg', median_blur_image)
```

---

### 🧾 **Summary of Output Files**

| Operation              | Output File Name            | Description                                  |
| ---------------------- | --------------------------- | -------------------------------------------- |
| Original Image         | `copy-hermoine_granger.png` | Grayscale copy of the original image         |
| Noisy Image            | `gauss-noisyimage.jpg`      | Image with Gaussian noise added              |
| Gaussian Blurred Image | `guassian_blur_image.jpg`   | Smoothed using Gaussian blur                 |
| Median Blurred Image   | `median_blur_image.jpg`     | Smoothed using Median blur (edge-preserving) |

---

### ✅ **Tips**

* You can visually compare `gauss-noisyimage.jpg`, `guassian_blur_image.jpg`, and `median_blur_image.jpg` to see the difference in noise reduction.
* Median Blur often preserves edges better than Gaussian Blur.

Let me know if you want to add **edge detection (e.g., using Canny)** or compare these visually using `matplotlib`.

Here's a complete, step-by-step walkthrough for **Exercise 4: Detecting People, Faces, and Eyes Using OpenCV** using Jupyter Notebook.

---

## ✅ **Exercise 4: Detect People in an Image Using OpenCV**

---

### 🛠️ **Task 1 - Import OpenCV and Load the Image**

#### Step 1: Install OpenCV (if not done yet)

In the **Jupyter Terminal**:

```bash
pip install opencv-python
```

#### Step 2: Create and Save the Notebook

* Create a new Python 3 notebook.
* Save it as: `Detecting people in an image.ipynb`.

#### Step 3: Import OpenCV and Load Image

```python
import cv2 as cv
```

#### Step 4: Download and Load the Face Image

In the terminal:

```bash
curl https://www.atwpl.com/learn_python/public/face_detection_orig.jpg > face_detection_orig.jpg
```

In the notebook:

```python
image = cv.imread('face_detection_orig.jpg')
cv.imwrite('copy-face_detection_orig.jpg', image)
```

---

### 🧍 **Task 2 - Detect Faces**

#### Step 1: Load Classifier and Convert to Grayscale

```python
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
```

#### Step 2: Detect Faces and Draw Rectangles

```python
faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv.imwrite('detected_faces.jpg', image)
```

---

### 👁️ **Task 3 - Detect Eyes**

#### Step 1: Load Eye Cascade and Detect Eyes

```python
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(gray_image, 1.1, 4)

for (x, y, w, h) in eyes:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imwrite('detected_eyes.jpg', image)
```

---

### 🧍‍♂️ **Task 4 - Detect Full Bodies (People)**

#### Step 1: Download and Load People Image

In the terminal:

```bash
curl https://atwpl.com/learn_python/public/people.jpg > people.jpg
```

In the notebook:

```python
people_image = cv.imread('people.jpg')
cv.imwrite('copy-people.png', people_image)
```

#### Step 2: Load Full Body Classifier and Detect People

```python
people_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_fullbody.xml')
people = people_cascade.detectMultiScale(people_image, 1.1, 2)

for (x, y, w, h) in people:
    cv.rectangle(people_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv.imwrite('detected_people.jpg', people_image)
```

---

### 📄 **Output Summary**

| Feature Detected   | Output Image          |
| ------------------ | --------------------- |
| Faces              | `detected_faces.jpg`  |
| Eyes               | `detected_eyes.jpg`   |
| People (full body) | `detected_people.jpg` |

---

### ✅ **Optional Enhancements**

You can use `matplotlib` to display the images directly in the notebook:

```python
from matplotlib import pyplot as plt
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
```

Let me know if you'd like to explore face recognition with **deep learning** (e.g., DNN or OpenCV's deep module) or work with **video streams** (live detection).

Here’s a **step-by-step implementation guide** for **Exercise 5 – Creating an Agent to Process Data Using Faust**, including all commands and code snippets.

---

## ✅ **Exercise 5: Creating a Faust Agent**

---

### 🧩 **Task 1: Install Faust & Start Kafka + Zookeeper**

---

#### 🔹 Step 1: Install Faust

In terminal:

```bash
pip install -U faust
```

#### 🔹 Step 2: Download and Extract Kafka

```bash
wget https://downloads.apache.org/kafka/2.7.0/kafka_2.12-2.7.0.tgz
tar -xvf kafka_2.12-2.7.0.tgz
```

#### 🔹 Step 3: Install Java (for Kafka/Zookeeper)

```bash
sudo apt install default-jre
```

#### 🔹 Step 4: Start Zookeeper

```bash
cd kafka_2.12-2.7.0
./bin/zookeeper-server-start.sh config/zookeeper.properties
```

#### 🔹 Step 5: Start Kafka Server (in a **new terminal tab**)

```bash
cd kafka_2.12-2.7.0
./bin/kafka-server-start.sh config/server.properties
```

---

### 🧠 **Task 2: Create a Faust Agent**

---

#### 🔹 Step 1: Create `faust_with_agents.py`

**File content:**

```python
import faust

class ReturnConcatenation(faust.Record):
    a: str
    b: str

app = faust.App('faust_with_agent', broker='kafka://localhost:9092')
topic = app.topic('adding', value_type=ReturnConcatenation)

@app.agent(topic)
async def concatenate(stream):
    async for value in stream:
        yield str(value.a) + " " + str(value.b)
```

💾 Save the file.

---

#### 🔹 Step 2: Start the Faust Worker

In terminal (same directory as your `.py` file):

```bash
~/.local/bin/faust -A faust_with_agents worker -l info
```

✅ You should see output confirming the Faust worker is running and listening to the topic `adding`.

---

### ✉️ **Task 3: Send Messages to the Agent**

---

#### 🔹 Step 1: Create `send_values_to_agent.py`

**File content:**

```python
import asyncio
from faust_with_agents import ReturnConcatenation, concatenate

async def send_value() -> None:
    print(await concatenate.ask(ReturnConcatenation(a="Hi", b="There")))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_value())
```

💾 Save the file.

---

#### 🔹 Step 2: Send the Message

In a new terminal tab:

```bash
python3 send_values_to_agent.py
```

✅ Output:

```bash
Hi There
```

---

### 🧪 **Verification Checklist**

| Component             | Working? | Notes                          |
| --------------------- | -------- | ------------------------------ |
| Zookeeper             | ✅        | Should be running on port 2181 |
| Kafka                 | ✅        | Should be running on port 9092 |
| Faust worker          | ✅        | Listens on `adding` topic      |
| Message sent & result | ✅        | `"Hi There"` printed           |

---

Would you like to see how to run Faust in Docker, or connect it to an external producer (like Kafka console or REST API)?

Here’s your complete guide for **Exercise 6 – Creating Timers for Repeated Operations in Faust**, including terminal commands and Python code for implementation.

---

## ✅ **Exercise 6: Creating Timers in Faust**

---

### 🧩 **Task 1 – Install Faust and Start Kafka + Zookeeper**

---

#### 🔹 Step 1: Install Faust

In your terminal:

```bash
pip install -U faust
```

#### 🔹 Step 2: Download and Extract Kafka

```bash
wget https://downloads.apache.org/kafka/2.7.0/kafka_2.12-2.7.0.tgz
tar -xvf kafka_2.12-2.7.0.tgz
```

#### 🔹 Step 3: Install Java (Required for Kafka)

```bash
sudo apt install default-jre
```

#### 🔹 Step 4: Start Zookeeper

```bash
cd kafka_2.12-2.7.0
./bin/zookeeper-server-start.sh config/zookeeper.properties
```

#### 🔹 Step 5: Start Kafka (In a new terminal)

```bash
cd kafka_2.12-2.7.0
./bin/kafka-server-start.sh config/server.properties
```

---

### ⏱️ **Task 2 – Create Timers for Repeated Operations**

---

#### 🔹 Step 1: Create the file `faust_with_timer.py`

In your text editor or IDE (e.g. PyCharm, VS Code), create a new file and add the following:

```python
import faust

app = faust.App('faust_app_with_timer', broker='kafka://localhost:9092')

@app.timer(interval=30)
async def every_thirty_seconds():
    print('You are working with Faust in Python')
```

💾 Save the file as `faust_with_timer.py`

---

#### 🔹 Step 2: Start Faust Worker

In the same directory as your script, run:

```bash
~/.local/bin/faust -A faust_with_timer worker -l info
```

📌 Output (every 30 seconds):

```
You are working with Faust in Python
```

✅ This confirms your Faust timer is working as expected.

---

### 🔁 **What’s Happening**

* `@app.timer(interval=30)` defines a periodic task.
* The function `every_thirty_seconds()` runs every 30 seconds after the worker starts.
* No Kafka topic or stream is needed — the timer is managed purely within the Faust app.

---

Would you like to modify this to:

* Run more frequently (e.g. every 5 seconds)?
* Add more complex periodic tasks like writing to a file or Kafka topic?

Let me know how you’d like to expand it!

