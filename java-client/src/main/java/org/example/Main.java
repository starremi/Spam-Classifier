package org.example;

import okhttp3.*;
import com.google.gson.*;

public class Main {
    public static void main(String[] args) throws Exception {
        OkHttpClient client = new OkHttpClient();
        Gson gson = new Gson();

        String apiUrl = "http://localhost:8000/predict";
        String text = (args.length > 0) ? String.join(" ", args)
                : "Congratulations! You won a free trip!";

        JsonObject body = new JsonObject();
        body.addProperty("message", text);

        Request request = new Request.Builder()
                .url(apiUrl)
                .post(RequestBody.create(
                        body.toString(), MediaType.parse("application/json")))
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                System.err.println("Request failed: " + response);
                return;
            }
            String json = response.body().string();
            JsonObject obj = gson.fromJson(json, JsonObject.class);
            String label = obj.get("label").getAsString();
            double score = obj.get("score").getAsDouble();
            System.out.printf("Prediction: %s (spam_prob=%.3f)%n", label, score);
        }
    }
}

