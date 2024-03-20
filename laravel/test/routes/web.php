<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\CRUDController;

Route::controller(CRUDController::class)->group(function(){;
    Route::get('/', 'index');
    Route::get('/crear', 'create');
});