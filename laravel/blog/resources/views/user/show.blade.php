@extends('layouts.plantilla')

@section('title', 'Show user')

@section('content')
    <h1>Este es el usuario que has creado.</h1>
    <a href="{{route('index')}}"> Volver al index</a>
    <br>
    <a href="{{route('user.edit')}}"> Editar usuario</a>
    
@endsection