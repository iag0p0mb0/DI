package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    private Button navegarAlDetalleButton;
    private Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);
        navegarAlDetalleButton = findViewById(R.id.navegarAlDetalle);//inicializamos el botón del xml
        navegarAlDetalleButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(context, DetailActivity.class);//Creamos un intent para poder nombrarlo en la función de StartActivity
                startActivity(intent);
            }
        });
    }
}