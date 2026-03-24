const BASE_URL = "http://YOUR_IP:8000";

export const detectFrame = async (base64) => {
  const res = await fetch(`${BASE_URL}/detect-frame/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ image: base64 }),
  });

  return res.json();
};