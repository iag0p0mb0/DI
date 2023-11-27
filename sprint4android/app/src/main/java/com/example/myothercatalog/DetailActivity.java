package com.example.myothercatalog;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
        //obtenemos la informacióndel intent
        AnimalData animal = getIntent().getParcelableExtra("animal");
        //referenciamos los elementos de la interfaz de usuario en el xml
        ImageView imageView = findViewById(R.id.imageView);
        TextView textTitle = findViewById(R.id.textTitle);
        TextView textDescription = findViewById(R.id.textDescription);
        //mostramos la información del animal en la interfaz de usuario
        textTitle.setText(animal.getName());
        textDescription.setText(animal.getDescription());

        //utilizamos Glide para cargar la imagen desde la URL y mostrarla en el ImageView
        Glide.with(this)
                .load(animal.getImage_url())
                .into(imageView);
    }
}
