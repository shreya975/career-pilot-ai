import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api/analyze",
});

export const flexibleAnalysis = async (formData) => {
  const response = await API.post("/flexible", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};
