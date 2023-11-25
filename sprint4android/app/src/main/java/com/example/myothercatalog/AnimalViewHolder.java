package com.example.myothercatalog;
import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class AnimalViewHolder extends RecyclerView.ViewHolder {

    // Declaración de variables miembro para los elementos de la vista en el ViewHolder
    private final TextView textView;
    private final ImageView imageView;

    // Constructor que toma una vista como parámetro (la vista de un elemento en el RecyclerView)
    public AnimalViewHolder(@NonNull View itemView) {
        // Llamar al constructor de la clase base (RecyclerView.ViewHolder)
        super(itemView);

        // Inicialización de las variables miembro con los elementos de la vista
        textView = (TextView) itemView.findViewById(R.id.animals_name_text_view);
        imageView = (ImageView) itemView.findViewById(R.id.animal_image_view);
    }

    // Método para mostrar datos en el ViewHolder
    public void showData(AnimalData data, Activity activity) {
        // Establecer el texto en el TextView con el nombre del animal
        textView.setText(data.getName());

        // Utilizar la biblioteca Glide para cargar la imagen desde la URL y mostrarla en el ImageView
        Glide.with(itemView.getContext())
                .load(data.getImage_url())
                .into(imageView);
    }
}