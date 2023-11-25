package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class AnimalRecyclerViewAdapter extends RecyclerView.Adapter<AnimalViewHolder> {
    // Lista que contiene todos los datos de animales
    private List<AnimalData> alltheData;
    // Actividad asociada al adaptador
    private Activity activity;
    private OnItemClickListener mListener;

    public interface OnItemClickListener {
        void onItemClick(int position);
    }
    public void setOnItemClickListener(OnItemClickListener listener) {
        mListener = listener;
    }
    // Constructor que recibe la lista de datos y la actividad
    public AnimalRecyclerViewAdapter(List<AnimalData> dataSet, Activity activity) {
        this.alltheData = dataSet;
        this.activity = activity;
    }
    // Método llamado cuando se necesita crear un nuevo ViewHolder
    @NonNull
    @Override
    public AnimalViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Inflar el diseño de la vista de un elemento y devolver un nuevo AnimalViewHolder
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.animal_view_holder, parent, false);
        return new AnimalViewHolder(view);
    }
    // Método llamado para actualizar la vista de un ViewHolder con datos específicos
    @Override
    public void onBindViewHolder(AnimalViewHolder holder, int position) {
        // Obtener los datos del animal en la posición actual
        AnimalData dataInPositionToBeRendered = alltheData.get(position);
        // Llamar al método showData del ViewHolder para mostrar los datos en la vista
        holder.showData(dataInPositionToBeRendered, activity);
        final int adapterPosition = holder.getAdapterPosition();

            holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (mListener != null && adapterPosition != RecyclerView.NO_POSITION) {
                    mListener.onItemClick(adapterPosition);
                }
            }
        });
    }
    // Método que devuelve la cantidad total de elementos en la lista de datos
    @Override
    public int getItemCount() {
        return alltheData.size();
    }
}