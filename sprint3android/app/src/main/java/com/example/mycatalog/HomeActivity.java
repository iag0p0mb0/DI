package com.example.mycatalog;

import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

import com.google.android.material.navigation.NavigationView;

public class HomeActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener{
    private DrawerLayout drawerLayout;
    private NavigationView navigationView;
    private MenuItem catalogItem;
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        //Establecemos la actionBar
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        //Establecemos el DrawerLayout
        drawerLayout = findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawerLayout.addDrawerListener(toggle);
        toggle.syncState();
        //Establecemos el NavigationView y su Listener
        navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(this);
        //Establecemos el header y el elemento seleccionado
        View header = navigationView.getHeaderView(0);
        header.findViewById(R.id.header_title).setOnClickListener(view -> Toast.makeText(
                HomeActivity.this,
                getString(R.string.title_click),
                Toast.LENGTH_SHORT).show());
        //Provocamos que el elemento Catalog del menú esté seleccionado de arranque
        catalogItem = navigationView.getMenu().getItem(0).getSubMenu().getItem(0);
        onNavigationItemSelected(catalogItem);
        catalogItem.setChecked(true);
    }
    //Creamos la función que haga que volvamos para atrás si le damos botón de atrás
    @Override
    public void onBackPressed() {
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }
    //Este método nos permite mostrar el Fragment del elemento seleccionado
    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
        if(menuItem.getItemId() != R.id.nav_catalog)
            //Si seleccionamos algún elemento distinto a Catalog, la primera vez,
            //deseleccionamos el elemento Catalog, para que ya no se siga mostrando coloreado (seleccionado)
            catalogItem.setChecked(false);
        showFragment(getTitle(menuItem));
        drawerLayout.closeDrawer(GravityCompat.START);
        return true;
    }

    //Hacemos un switch que mande el id del elemento seleccionado
    private int getTitle(@NonNull MenuItem menuItem) {
        String nombre = String.valueOf(menuItem.getTitle());
        switch (nombre) {
            case "Catalog":
                return R.string.menu_catalog;
            case "About":
                return R.string.menu_about;
            default:
                throw new IllegalArgumentException("That option isn't implement!!");
        }
    }

    //Este método hace que según el id del elemento pulsado, mostramos su respectivo Fragment con su título en la barra superior
    private void showFragment(@StringRes int titleId){
        if (titleId == R.string.menu_catalog) {
            Fragment fragment = FragmentCatalog.newInstance(titleId);
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.home_content, fragment)
                    .commit();
            setTitle(getString(titleId));

        }else if(titleId == R.string.menu_about) {
            Fragment fragment = FragmentAbout.newInstance(titleId);
            getSupportFragmentManager()
                    .beginTransaction()
                    .replace(R.id.home_content, fragment)
                    .commit();
            setTitle(getString(titleId));
        }
    }
}
