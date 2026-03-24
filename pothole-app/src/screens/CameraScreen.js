import { CameraView, useCameraPermissions } from 'expo-camera';
import { useRef, useState, useEffect } from 'react';
import { View, Text, Button } from 'react-native';
import BoundingBoxes from '../components/BoundingBoxes';

export default function CameraScreen() {
  const cameraRef = useRef(null);
  const [permission, requestPermission] = useCameraPermissions();
  const [boxes, setBoxes] = useState([]);

  useEffect(() => {
    if (!permission) requestPermission();
  }, []);

  if (!permission?.granted) {
    return (
      <View>
        <Text>No camera permission</Text>
        <Button title="Allow Camera" onPress={requestPermission} />
      </View>
    );
  }

  return (
    <View style={{ flex: 1 }}>
      <CameraView
        ref={cameraRef}
        style={{ flex: 1 }}
        facing="back"
      />

      <BoundingBoxes boxes={boxes} />
    </View>
  );
}