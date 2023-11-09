package com.example.mycatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

public class FragmentCatalog extends Fragment {
    private Button button;
    private Context context;
    public static FragmentCatalog newInstance(@StringRes int textId) {
        FragmentCatalog frag = new FragmentCatalog();
        return frag;
    }
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable
    Bundle savedInstanceState) {
        View layout = inflater.inflate(R.layout.fragment_catalog, container, false);
        button = layout.findViewById(R.id.buttonGoToDetail1);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Intent y startActivity que inicializan la actividad de DetailActivity,
                // al pulsar el botón del FragmentCatalog.
                Intent intentDetailActivity = new Intent(context, DetailActivity.class);
                // Enviaremos un Bundle con la variable número de likes a la DetailActivity
                Bundle bundle = new Bundle();
                bundle.putInt("likes",0);
                intentDetailActivity.putExtras(bundle);
                // Iniciamos DetailActivity con dicho Bundle
                startActivity(intentDetailActivity);
            }
        });

        return layout;
    }
    // Método que permite guardar el context del Fragment:
    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        this.context = context;
    }
}