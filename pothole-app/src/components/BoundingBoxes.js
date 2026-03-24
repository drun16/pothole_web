import { View } from "react-native";

export default function BoundingBoxes({ boxes }) {
  return (
    <View style={{ position: "absolute", top: 0, left: 0 }}>
      {boxes.map((box, i) => (
        <View
          key={i}
          style={{
            position: "absolute",
            left: box.x1,
            top: box.y1,
            width: box.x2 - box.x1,
            height: box.y2 - box.y1,
            borderWidth: 2,
            borderColor: "red",
          }}
        />
      ))}
    </View>
  );
}