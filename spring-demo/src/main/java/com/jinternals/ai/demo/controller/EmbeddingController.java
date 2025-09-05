package com.jinternals.ai.demo.controller;

import com.jinternals.ai.demo.controller.request.EmbedRequest;
import com.jinternals.ai.demo.controller.response.EmbedResponse;
import com.jinternals.ai.demo.services.EmbeddingService;
import lombok.AllArgsConstructor;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/embed")
@Validated
@AllArgsConstructor
public class EmbeddingController {

    private final EmbeddingService service;

    @PostMapping
    public EmbedResponse embed(@RequestBody EmbedRequest body) {
        float[] embedding = service.createEmbedding(body.text());
        return new EmbedResponse(embedding);
    }


}
