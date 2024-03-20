@extends('layouts.plantilla')

@section('title', 'Index')

@section('content')
    <h1>Bienvenido al index de la página</h1>
    <a href="{{route('user.create')}}">Crear usuario</a>
    <ul>
        @foreach ($usuarios as $usuario) 
            <li> {{$usuario->nombre}}</li>
        @endforeach
    </ul>

    {{$usuarios->links()}}
@endsection

