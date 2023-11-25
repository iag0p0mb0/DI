package com.example.myothercatalog;
import org.json.JSONException;
import org.json.JSONObject;

public class AnimalData {

    // Variables miembro para almacenar información sobre el animal
    private String name;
    private String description;
    private String image_url;

    // Constructor que toma un objeto JSONObject como parámetro
    public AnimalData(JSONObject json) {
        try {
            // Inicialización de las variables miembro con los valores del JSONObject
            this.description = json.getString("description");
            this.name = json.getString("name");
            this.image_url = json.getString("image_url");
        } catch (JSONException e) {
            // Manejo de excepciones en caso de que ocurra un error al obtener los valores del JSONObject
            e.printStackTrace();
        }
    }

    // Método para obtener el nombre del animal
    public String getName() {
        return name;
    }

    // Método para obtener la descripción del animal
    public String getDescription() {
        return description;
    }

    // Método para obtener la URL de la imagen del animal
    public String getImage_url() {
        return image_url;
    }
}
