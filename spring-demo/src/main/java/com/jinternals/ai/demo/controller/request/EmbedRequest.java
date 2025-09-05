package com.jinternals.ai.demo.controller.request;

import jakarta.validation.constraints.NotBlank;

public record EmbedRequest(@NotBlank String text) {}

