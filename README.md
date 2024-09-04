# smartBikeLock

  BANDv1_3: is the micropython code for the arm band device
  
  LOCKv1_3: is the micropython code for the bike lock device
  
  The micropython code can be copied into a Raspberry Pi Pico W and can run if the sensors and modules setup is done. Thonny, or other similar editor, can be used to edit and run the code.
bike_lock.zip.part1 and bike_lock.zip.part2 files are compressed files of the mobile applications Flutter project, they need to be decompressed and merged into the same directory (I used Visual Studio Code to edit and run the project). A mobile emulator or an Android device with USB Debugging enabled can be used to run the Application.

  Below is a step by step instruction procedure to follow to run the project (the procedure is AI generated based on my project specifications):
  
# Steps to Run a Flutter Project

## Prerequisites

1. **Install Flutter SDK**:
   - Download and install the Flutter SDK from the official Flutter website: https://flutter.dev/docs/get-started/install
   - Follow the platform-specific instructions (Windows, macOS, Linux) to install and set up the SDK.

2. **Install Android Studio (for Android development)**:
   - Download and install Android Studio: https://developer.android.com/studio
   - During installation, make sure to install the Android SDK, Android SDK Platform-Tools, and Android Virtual Device (AVD) Manager.
   - Set up an Android emulator or connect a physical Android device for testing.

3. **Set up an editor**:
   - **Visual Studio Code (VS Code)**: Install the Dart and Flutter extensions from the VS Code marketplace.
   - **Android Studio**: Flutter plugin and Dart plugin should be installed by default, or you can install them via the Plugins settings.

4. **Check Environment Setup**:
   - Run `flutter doctor` in your terminal to check if all the required tools are properly installed. Resolve any issues that are reported.

## Steps to Run the Project

1. **Download the Project Files**:
   - If you have the project files in a zip or any other archive format, extract them to your desired directory.

2. **Navigate to the Project Directory**:
   - Open your terminal (Command Prompt, PowerShell, or terminal on macOS/Linux).
   - Navigate to the project folder:
     ```bash
     cd path/to/your/flutter/project
     ```

3. **Get the Project Dependencies**:
   - Run the following command to fetch all the dependencies the project requires:
     ```bash
     flutter pub get
     ```

4. **Connect a Device or Start an Emulator**:
   - **Connect a Physical Device**: Connect your Android device via USB. Ensure USB debugging is enabled on the device.
   - **Start an Emulator**: If you prefer to use an Android emulator:
     - Open Android Studio and launch an emulator via the AVD Manager.
     - Alternatively, start an emulator from the terminal:
       ```bash
       flutter emulators --launch <emulator-id>
       ```
     - To list available emulators:
       ```bash
       flutter emulators
       ```

5. **Run the Project**:
   - **Via VS Code**:
     - Open the project directory in VS Code.
     - Ensure the connected device or emulator is selected in the bottom-right device dropdown.
     - Press `F5` or click on the green "Run" button to start the project.
   - **Via Android Studio**:
     - Open the project in Android Studio.
     - Select the target device from the device dropdown menu at the top.
     - Click on the green play button (or `Shift + F10`) to run the app.
   - **Via Terminal**:
     - Run the following command:
       ```bash
       flutter run
       ```

6. **Debugging and Logging**:
   - Use the terminal or the Debug Console in your IDE to view logs and debug information.
   - You can use breakpoints, inspect variables, and step through the code using the debugging tools in VS Code or Android Studio.

## Optional: Modify Configuration

- If needed, configure your project settings (e.g., package name, app icon) in the `android` or `ios` folders.
- Update `pubspec.yaml` if you need to add or update dependencies.

## After Running

- Once the app is running, interact with it on the connected device or emulator.
- Make code changes and use Hot Reload (`r` in terminal, `Ctrl + S` in VS Code) to see the changes instantly without restarting the app.
