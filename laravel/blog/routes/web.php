<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\UsuarioController;

/*Route::get('/', function () {
    return view('welcome');
});
*/
Route::get('/', HomeController::class, '');

Route::get('/', [UsuarioController::class, 'index'])->name('index');
Route::get('/create', [UsuarioController::class, 'create'])->name('user.create');
Route::post('/create', [UsuarioController::class, 'submit'])->name('user.submit');
Route::get('/{usuario}', [UsuarioController::class, 'show'])->name('user.show');
Route::get('/delete', [UsuarioController::class, 'delete'])->name('user.delete');
Route::get('/{id}/edit', [UsuarioController::class, 'edit'])->name('user.edit'); 


