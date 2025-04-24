import time
import psutil
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def set_tf2_volume_on_launch(target_volume=0.05):  # 0.05 = 5% volume
    tf2_found = False
    
    while not tf2_found:
        # Get all running processes
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if process.info['name'].lower() == 'tf_win64.exe':
                    # Wait a brief moment for the audio session to initialize
                    time.sleep(2)
                    
                    # Get all audio sessions
                    sessions = AudioUtilities.GetAllSessions()
                    
                    # Find TF2's audio session
                    for session in sessions:
                        if session.Process and session.Process.name().lower() == 'tf_win64.exe':
                            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                            volume.SetMasterVolume(target_volume, None)
                            print(f"Set TF2 initial volume to {target_volume * 100}%")
                            tf2_found = True
                            return  # Exit the function after setting the volume
                            
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
        time.sleep(1)  # Check every second until TF2 is found

if __name__ == "__main__":
    try:
        set_tf2_volume_on_launch()
    except KeyboardInterrupt:
        print("\nScript stopped by user")
		
		
		
		