package main

import "testing"

func TestGetGreeting(t *testing.T){

	expected := "Hello World!"

	actual := getGreeting()

	if actual := expected {
		t.Errorf("Тест провален", expected, actual)
	}
}