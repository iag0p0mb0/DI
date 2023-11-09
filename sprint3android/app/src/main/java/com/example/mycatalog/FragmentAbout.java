package com.example.mycatalog;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;
public class FragmentAbout extends Fragment {
    public static FragmentAbout newInstance(@StringRes int textId) {
        FragmentAbout frag = new FragmentAbout();
        return frag;
    }
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable
    Bundle savedInstanceState) {
        View layout = inflater.inflate(R.layout.fragment_about, container, false);

        return layout;
    }
}