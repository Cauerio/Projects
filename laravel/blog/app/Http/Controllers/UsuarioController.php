<?php

namespace App\Http\Controllers;
use App\Models\User;
use Illuminate\Http\Request;
class UsuarioController extends Controller
{
    public function index()
    {
        $usuarios = User::orderBy('nombre', 'desc')->paginate(); 
        return view('index', compact('usuarios'));
    }

    public function create()
    {
        return view('user.create');
    }

    public function submit(Request $request){
        #devuelve el posteo en formato json
        //return $request->all();

        //requisitos
        $request->validate([
            'nombre'=>'required',
            'apellido' => 'required',
            'email' => 'required',
            'password' => 'required|min:8'
        ]);

        $usuario = new User();

        $usuario->nombre = $request->nombre;
        $usuario->apellido = $request->apellido;
        $usuario->email = $request->email;
        $usuario->password = $request->password;

        $usuario-> save();

        return redirect()->route('user.show', $usuario->id);
    }

    public function show(User $usuario)
    {
        return view('user.show', compact('usuario'));

    }

    public function delete()
    {
        return view('user.delete');
    }

    public function edit(Request $request, User $usuario){
        return view('user.edit');

        //requisitos
        $request->validate([
            'email' => 'required',
            'password' => 'required|min:8'
        ]);
    }
}
