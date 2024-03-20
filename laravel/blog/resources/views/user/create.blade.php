@extends('layouts.plantilla')

@section('title', 'Create user')

@section('content')
    <h1>Bienvenido al creador de usuarios de la página</h1>
    <a href="{{route('user.edit')}}"> Editar usuario</a>

    <form action="{{route('user.submit')}}" method="POST">

        @csrf

    <label>
        Nombre:
        <br>
        <input type="text" name="nombre" value="{{old('nombre')}}">
    </label>

    @error('nombre')
    <br>
        <span>*{{$message}}</span>
    <br>
    @enderror

    <br>
    <label> 
        Apellido:
        <br>
        <input type="text" name="apellido" value="{{old('apellido')}}">
    </label>

    @error('apellido')
    <br>
        <span>*{{$message}}</span>
    <br>
    @enderror

    <br>
    <label>
        Correo electronico:
        <br>
        <input type="text" name="email" value="{{old('email')}}">
    </label>

    @error('email')
    <br>
        <span>*{{$message}}</span>
    <br>
    @enderror

    <br>
    <label>
        Contraseña:
        <br>
        <input type="text" name="password" value="{{old('password')}}">
    </label>

    @error('password')
    <br>
        <span>*{{$message}}</span>
    <br>
    @enderror
<br>
<br>
    <button type="submit">Enviar</button>
</form>
@endsection

