package com.example.myothercatalog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.ListAdapter;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private ListAdapter listAdapter;
    private RecyclerView.Adapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Obtener referencia al RecyclerView desde el diseño de la actividad
        RecyclerView recyclerView = findViewById(R.id.recyclerView);

        // Crear referencia a la actividad actual
        Activity activity = this;

        // Crear una solicitud JSON utilizando Volley
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/iag0p0mb0/DI/main/resources/catalog.json",
                null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        // Procesar la respuesta JSON exitosa
                        List<AnimalData> allAnimals = new ArrayList<>();

                        // Iterar a través de los elementos en el JSON Array
                        for (int i = 0; i < response.length(); i++) {
                            try {
                                // Obtener un objeto AnimalData a partir de cada objeto JSON
                                JSONObject animal = response.getJSONObject(i);
                                AnimalData animals = new AnimalData(animal);
                                allAnimals.add(animals);
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }

                        // Crear un adaptador personalizado y configurarlo en el RecyclerView
                        AnimalRecyclerViewAdapter adapter = new AnimalRecyclerViewAdapter(allAnimals, activity);
                        recyclerView.setAdapter(adapter);

                        // Configurar un LinearLayoutManager para el RecyclerView
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                        // Configurar el oyente de clics después de haber establecido el adaptador y el LayoutManager
                        adapter.setOnItemClickListener(new AnimalRecyclerViewAdapter.OnItemClickListener() {
                            @Override
                            public void onItemClick(int position) {
                                AnimalData clickedAnimal = allAnimals.get(position);
                                // Iniciar la nueva actividad
                                Intent intent = new Intent(MainActivity.this, DetailActivity.class);
                                // Puedes pasar datos adicionales a la nueva actividad si es necesario
                                // intent.putExtra("clave", valor);
                                intent.putExtra("animal",clickedAnimal);
                                startActivity(intent);
                            }
                        });
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Manejar errores de la solicitud y mostrar un mensaje de tostada
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
        );

        // Crear una cola de solicitudes Volley y agregar la solicitud a la cola
        RequestQueue queue = Volley.newRequestQueue(this);
        queue.add(request);
    }
}